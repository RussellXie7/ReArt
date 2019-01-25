/**
 * Created by chenyang on 10/1/16.
 */

var data = require("../data.json");
var sessionList = data["session"];


exports.view = function(req, res){
    var currentSession = req.query.sessionID;
    var newSession = {};

    newSession["sessionID"] = currentSession;

    res.render('preview', newSession);
};