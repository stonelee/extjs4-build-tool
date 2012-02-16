extjs4-build-tool
========

#### build tool for Ext JS 4 ####

The aim of the project is to build model, store, view, controller js files of app folder and app.js into one packed js file.
Just for using in production.

### Usage ###

Download the [build tool](https://github.com/stonelee/extjs4-build-tool/zipball/master) and include it in your Ext JS 4 project.
project document architecture is as follows:

```
|app
|--controller
|--model
|--store
|--view
|build-tool
|all.js
```

then

```bash
$ python run.py
```

will create:

* app.jsb3      file paths
* all-debug.js  unpacked file,used for debug
* all.js        packed file,used in production

create your index.html used in production

```html
<!DOCTYPE HTML>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="extjs/ext-all.css">
</head>
<body>
	<script type="text/javascript" src="extjs/ext-all.js"></script>
	<script type="text/javascript" src="all.js"></script>
</body>
</html>
```

