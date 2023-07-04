const ejs = require('ejs');

let data = '{"Ok":1}';

ejs.renderFile('greet', {
    ...JSON.parse(data),
    cache: false
});