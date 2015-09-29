var libraryServices = angular.module('libraryServices', ['ngResource']);


//libraryServices.factory('Library', ['$resource',
//    function($resource) {
//        return $resource('/libraries/:libraryId.json', {}, {
//           query: {method:'GET', isArray:true}
//        });
//}]);

libraryServices.factory('Library', function($resource) {
   return $resource('/libraries/:libraryId.json');
});