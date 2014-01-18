/*
Contains environment settings for the Jasmine tests.
 */

// The root directory for javascript files
// Feel free to overwrite this if it isnt working!
// process.cwd() should point to the root of the project
var srcRoot =  process.cwd() + "/src/static/js/";


var fs = require('fs');
var vm = require('vm');

exports.srcRoot = srcRoot;

// assembles a path relative to the root dir
exports.path = function(fn) {
	return( srcRoot + fn );
}

// imports a normal javascript file into the nodejs environment and processes the file
exports.importJS = function(fn) {
	var filedata = fs.readFileSync(fn,'utf-8');
	vm.runInThisContext(filedata)
}


