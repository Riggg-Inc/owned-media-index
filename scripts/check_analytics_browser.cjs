const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright-core');
const fs = require('fs'), http = require('http'), path = require('path'), assert = require('assert');
const root = path.resolve(process.env.OMI_SITE_DIR || 'site');
const server = http.createServer((req,res)=>{
 let file = path.join(root, new URL(req.url,'http://localhost').pathname);
 if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file,'index.html');
 if(!file.startsWith(root)||!fs.existsSync(file)){res.writeHead(404);return res.end();}
 const ext=path.extname(file);res.setHeader('Content-Type',({'.html':'text/html','.js':'application/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'})[ext]||'application/octet-stream');
 res.end(fs.readFileSync(file));
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const base=process.env.OMI_TEST_URL || 'http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_EXECUTABLE || undefined,headless:true});
 try {
 const context=await browser.newContext();const page=await context.newPage();
 let requests=[],responses=[],errors=[];
 page.on('request',r=>{if(/google-analytics.com|googletagmanager.com/.test(r.url()))requests.push({url:r.url(),body:r.postData()});});
 page.on('response',r=>{if(/google-analytics.com|googletagmanager.com/.test(r.url()))responses.push({url:r.url(),status:r.status()});});
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(base,{waitUntil:'networkidle'});
 console.log('consent form',await page.locator('form[name="consent"]').innerText());
 assert.equal(requests.length,0,'no analytics before consent');
 await page.locator('form[name="consent"] button[type="reset"]').click();
 await page.waitForLoadState('networkidle');
 assert.equal(requests.length,0,'no analytics on rejection');
 await page.reload({waitUntil:'networkidle'});
 assert.equal(requests.length,0,'rejection persists');
 await page.evaluate(()=>localStorage.clear());
 await page.goto(base,{waitUntil:'networkidle',referer:'https://www.google.com/search?q=private-test-query'});
 if (await page.locator('form[name="consent"] label[for="__settings"]').isVisible()) await page.locator('form[name="consent"] label[for="__settings"]').click();
 await page.locator('form[name="consent"] label.task-list-control').filter({has:page.locator('input[name="analytics"]')}).click();
 assert(await page.locator('form[name="consent"] input[name="analytics"]').isChecked());
 await page.locator('form[name="consent"] button:not([type="reset"])').click();
 await page.waitForResponse(r=>/google-analytics.com.*collect/.test(r.url()),{timeout:30000});
 await page.waitForLoadState('networkidle');
 let layer=await page.evaluate(()=>window.dataLayer.map(a=>Array.from(a)));
 assert.equal(layer.filter(x=>x[0]==='event'&&x[1]==='page_view').length,1,'one explicit pageview');
 assert.equal(layer.find(x=>x[0]==='event'&&x[1]==='page_view')[2].page_referrer,'https://www.google.com/search','original referrer survives consent reload without query');
 // Observe the real outbound anchor click but cancel navigation to retain event evidence.
 await page.evaluate(()=>document.addEventListener('click',e=>{if(e.target.closest('a[href="https://riggg.com"]'))e.preventDefault();}));
 await page.locator('a[href="https://riggg.com"]').first().click();
 await page.waitForTimeout(1500);
 layer=await page.evaluate(()=>window.dataLayer.map(a=>Array.from(a)));
 assert(layer.some(x=>x[0]==='event'&&x[1]==='riggg_visit'));
 const acceptedRequestCount=requests.length;
 await page.reload({waitUntil:'networkidle'});
 await page.waitForTimeout(1500);
 assert(requests.length>acceptedRequestCount,'acceptance persists');
 await page.getByText('Analytics preferences',{exact:true}).click();
 await page.locator('form[name="consent"] button[type="reset"]').click();
 await page.waitForLoadState('networkidle');
 const before=requests.length;
 await page.reload({waitUntil:'networkidle'});
 await page.waitForTimeout(1500);
 assert.equal(requests.length,before,'withdrawal stops new requests on reload');
 const report={base,passed:true,requests,responses,errors,checks:['no analytics before choice','reject and persist','opt in sends GA collection','one explicit pageview','riggg_visit click','accept persists','withdraw/reload stops analytics']};
 if (process.env.OMI_TEST_REPORT) fs.writeFileSync(process.env.OMI_TEST_REPORT,JSON.stringify(report,null,2));
 console.log(JSON.stringify(report,null,2));
 } finally {await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exit(1)});
