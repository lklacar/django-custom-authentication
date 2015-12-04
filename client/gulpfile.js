var browserify = require('browserify');
var watchify = require('watchify');
var gulp = require('gulp');
var source = require('vinyl-source-stream');
var sourceFile = './src/main.js';
var destFolder = '../static/js';
var destFile = 'app.js';

gulp.task('browserify', function () {
    return browserify(sourceFile)
        .bundle()
        .pipe(source(destFile))
        .pipe(gulp.dest(destFolder));
});


gulp.task('default', ['browserify']);