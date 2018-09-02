fs.writeFile('save.html', document.body.innerHTML, function (err) {
  if (err) throw err;
  console.log('Saved!');
});
