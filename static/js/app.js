var phonecatApp = angular.module('libraryApp', [
    'ngRoute',
    'libraryControllers',
    'libraryFilters',
    'libraryServices',
    'bookControllers',
]);

phonecatApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'static/partials/library-list.html',
                controller: 'LibraryListCtrl'
            }).
            when('/libraries', {
                templateUrl: 'static/partials/library-list.html',
                controller: 'LibraryListCtrl'
            }).
            when('/libraries/:libraryId', {
                templateUrl: 'static/partials/library-detail.html',
                controller: 'LibraryDetailCtrl'
            }).
//            when('/phones', {
//                templateUrl: 'static/partials/phone-list.html',
//                controller: 'PhoneListCtrl'
//            }).
//            when('/phones/:phoneId', {
//                templateUrl: 'static/partials/phone-detail.html',
//                controller: 'PhoneDetailCtrl'
//            }).
            otherwise({
                redirectTo: '/libraries'
            });
    }
]);