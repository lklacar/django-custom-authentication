// Imports
var browserify = require('browserify');
var watchify = require('watchify');
var gulp = require('gulp');
var source = require('vinyl-source-stream');
var uglify = require('gulp-uglify');
var buffer = require('vinyl-buffer');

// Settings
var sourceFile = './src/main.js';
var destFolder = '../static/js';
var destFile = 'app.js';
var production = false; // Should the output be minimized


// Task
gulp.task('browserify', function () {
    var bundler = browserify(sourceFile)
        .bundle()
        .pipe(source(destFile));
    if (production) {
        return bundler
            .pipe(buffer())
            .pipe(uglify())
            .pipe(gulp.dest(destFolder))
    }
    return browserify(sourceFile)
        .bundle()
        .pipe(source(destFile))
        .pipe(gulp.dest(destFolder))
});


gulp.task('default', ['browserify']);