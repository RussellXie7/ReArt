//dependencies for each module used
var express = require('express');
var app = express();
var http = require('http').createServer(app);
var path = require('path');
var fs = require('fs');
var formidable = require('formidable');


var handlebars = require('express-handlebars');
var dotenv = require('dotenv');

dotenv.load();

var router = {
    home: require("./routes/home"),
    preview: require('./routes/preview'),
    loading: require('./routes/loading'),
    share: require('./routes/share')
};

app.set('port', 80);

app.engine('handlebars', handlebars());
app.set('view engine', 'handlebars');

app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

//routes
app.get('/', router.home.view);
app.get('/preview', router.preview.view);
app.get('/loading', router.loading.view);
app.get('/share', router.share.view);

app.post('/upload', function(req, res){

    // create an incoming form object
    var form = new formidable.IncomingForm();

    var sessionID = req.query.sessionID;
    var inputMOVName = sessionID + ".MOV";

    // specify that we want to allow the user to upload multiple files in a single request
    form.multiples = true;

    // store all uploads in the /uploads directory
    form.uploadDir = path.join(__dirname, '/user-uploads');

    // every time a file has been uploaded successfully,
    // rename it to it's orignal name
    form.on('file', function(field, file) {
        fs.rename(file.path, path.join(form.uploadDir, inputMOVName));
    });

    // log any errors that occur
    form.on('error', function(err) {
        console.log('An error has occured: \n' + err);
    });

    // once all the files have been uploaded, send a response to the client
    form.on('end', function() {
        res.end('success');
    });

    // parse the incoming request containing the form data
    form.parse(req);

});


http.listen(app.get('port'), function() {
    console.log('Express server listening on port ' + app.get('port'));
});
