/**
 * Created by chenyang on 10/1/16.
 */

var data = require("../data.json");
var sessionList = data["session"];
var spawn = require("child_process").spawn;


exports.view = function(req, res){
    var currentSession = req.query.sessionID;



    res.render('share');
};