//var phonecatControllers = angular.module('phonecatControllers', []);
//
//phonecatControllers.controller('PhoneListCtrl', ['$scope', 'Phone', function($scope, Phone) {
//    $scope.phones = Phone.query();
//    $scope.orderProp = 'age';
//}]);
//
//phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone', function($scope, $routeParams, Phone) {
//    $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
//        $scope.mainImageUrl = 'static/' + phone.images[0];
//    });
//
//    $scope.setImage = function(imageUrl) {
//        $scope.mainImageUrl = imageUrl;
//    }
//}]);

// http://www.sitepoint.com/creating-crud-app-minutes-angulars-resource/

var libraryControllers = angular.module('libraryControllers', []);

libraryControllers.controller('LibraryListCtrl', ['$scope', 'Library', function($scope, Library) {
    var libraries = Library.query(function(data) {
        console.log(data)
    });
    $scope.libraries = libraries;
}]);

libraryControllers.controller('LibraryDetailCtrl', ['$scope', '$routeParams', 'Library', function($scope, $routeParams, Library) {
    var library = Library.get({libraryId: $routeParams.libraryId}, function(data) {
        console.log(data)
    });
    $scope.library = library;

    $scope.search = function() {
        alert("llll");
    };
}]);

var bookControllers = angular.module('bookControllers', []);

bookControllers.controller('BookSearchCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.search = function() {
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        $http({
            method: 'POST',
            url: '/api/books/search',
            data: $.param({
                'query': $scope.query
            }),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(data) {
            $scope.books = data;
            console.log(data);
        });
    };
}]);