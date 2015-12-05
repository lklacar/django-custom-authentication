'use strict';

/* App Module */
var angular = require('angular');
var route = require('angular-route');


var app = angular.module('app', [
    'ngRoute'
]);

app.config(['$routeProvider', '$locationProvider',
    function ($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(false);

        $routeProvider.
        when('/phones', {
            templateUrl: 'angular/list',
            controller: 'PostListController'
        }).
        when('/phones/:phoneId', {
            templateUrl: 'post-detail.html',
            controller: 'PostDetailController'
        })

    }]);


app.controller('PostListController', ['$scope', '$http',
    function ($scope, $http) {


    }]
);

app.controller('PhoneDetailCtrl', ['$scope', '$routeParams',
    function ($scope, $routeParams) {


    }]
);



