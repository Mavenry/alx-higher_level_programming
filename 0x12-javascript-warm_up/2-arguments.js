#!/usr/bin/node

const args = process.argv;
const argCount = args.length - 2;

if (argCount === 0){
	console.log("No Argument");
} else if (argCount === 1) {
	console.log("Argument found");
} else if (argCount > 1) {
	console.log("Arguments found");
}
