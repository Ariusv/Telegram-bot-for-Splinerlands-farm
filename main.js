require('dotenv').config();
const { run, setupAccount } = require('./index');
const { sleep } = require('./helper');
const chalk = require('chalk');



async function startSingle() {
    let account = process.env.ACCOUNT;
    let password = process.env.PASSWORD;
    setupAccount(account, password);
    await run();
}

(async()=> {
        await startSingle();
})()