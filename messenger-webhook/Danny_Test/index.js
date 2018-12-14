const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const verificationController = require('./controllers/verfication');
const messageWebhookController = require('./controllers/messageWebhook');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.get('/', verificationController);
app.post('/', messageWebhookController);

app.listen(3000, () => console.log("Webhook server is listening, port 3000"));

