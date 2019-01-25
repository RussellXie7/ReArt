/**
 * Created by chenyang on 10/1/16.
 */

var data = require("../data.json");
var sessionList = data["session"];
var spawn = require("child_process").spawn;


exports.view = function(req, res){

    res.render('loading');

    console.log("in loading");

    var styleImg = req.query.optionImg;
    var currentSession = req.query.sessionID;

    var moivePath = "user-uploads/" + currentSession + ".MOV";

    var fps = 3;
    var stylePath = "~/sdhacks_server/static_files/" + styleImg + ".jpg";

    var python = spawn('python', ["~/sdhacks_server/neural-style/MainController.py", moivePath, fps, stylePath]);

    var output = "";
    python.stdout.on('data', function(data){ output += data });
    python.on('close', function(code){
        console.log(code)
        if (code !== 0) {
            // return res.send(500, code);
        }
        // return res.send(200, output);
    });

};