var PythonShell = require('python-shell');

PythonShell.run('./firebaseApiCall.py', function (err) {
  if (err) throw err;
  console.log('finished');
});
