var libraryFilters = angular.module('libraryFilters',[]);

libraryFilters.filter('checkmark', function() {
    return function(input) {
        return input ? '\u2713' : '\u2718';
    };
});

