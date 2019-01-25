/**
 * Created by chenyang on 10/1/16.
 */

var data = require("../data.json");
var sessionList = data["session"];


exports.view = function(req, res){

    var sessionID = Date.now();
    var newSession = {};

    newSession["sessionID"] = sessionID;

    res.render('home', newSession);
};