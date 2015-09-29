var phonecatApp = angular.module('libraryApp', [
    'ngRoute',
    'libraryControllers',
    'libraryFilters',
    'libraryServices'
]);

phonecatApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/libraries', {
                templateUrl: 'static/partials/library-list.html',
                controller: 'LibraryListCtrl'
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