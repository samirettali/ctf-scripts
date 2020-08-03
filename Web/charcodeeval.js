#!/usr/bin/env node

// A simple script that encodes the first argument to an
// `eval(String.fromCharCode())`

var payload = process.argv[2];
console.log('Encoding ' + payload);

var encodedPayload = [];
for (var i = 0; i < payload.length; i++) {
    encodedPayload.push(payload.charCodeAt(i));
}

process.stdout.write('eval(String.fromCharCode(' + encodedPayload.join(',') + '))\n');
