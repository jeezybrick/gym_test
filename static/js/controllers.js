/**
 * Created by user on 05.10.15.
 */

angular
    .module('myApp')
    .controller('HomeController', HomeController);

function HomeController($scope, $timeout, AuthUser, Booking, MyBookings, Flash, $auth) {
    $scope.selectedDate = false;

    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();

    $scope.user = AuthUser; // Auth user object
    $scope.startPageLoad = false;
    $scope.bookingLoad = false;
    $scope.addOrderMessageSuccess = 'Approved!';
    $scope.selectedDate = moment(date).format('YYYY-MM-DD');

    $scope.delay = $timeout(function () {

        $scope.startPageLoad = true;

    }, 400);

    /* alert on eventClick */
    $scope.alertOnEventClick = function(date, jsEvent, view){

        $scope.alertMessage = (date.format() + ' was clicked ');
        $scope.selectedDate = date.format();
    };

    $scope.isUserAuth = function () {
        return $scope.user.id;
    };
     /* config object */
    $scope.uiConfig = {
        calendar: {
            height: 450,
            editable: true,
            header: {
                left: '',
                center: 'title',
                right: 'today prev,next'
            },
            dayClick: $scope.alertOnEventClick,
            eventDrop: $scope.alertOnDrop,
            eventResize: $scope.alertOnResize,
            //defaultView: 'basicWeek'
        }
    };

    $scope.events = [
      {title: 'All Day Event',start: new Date(y, m, 1)},
      {title: 'Long Event',start: new Date(y, m, d - 5),end: new Date(y, m, d - 2)},
      {id: 999,title: 'Repeating Event',start: new Date(y, m, d - 3, 16, 0),allDay: true},
      {id: 999,title: 'Repeating Event',start: new Date(y, m, d + 4, 16, 0),allDay: false},
      {title: 'Birthday Party',start: new Date(y, m, d + 1, 19, 0),end: new Date(y, m, d + 1, 22, 30),allDay: false}
    ];

    /**
     * Get list of bookings for auth user
     */
    if ($scope.isUserAuth()) {

        $scope.booking = Booking.query(function () {

            $scope.bookingLoad = true;

        }, function () {
            $scope.bookingLoadError = true;
        });

    }


    /**
     * Add order
     */
    $scope.makeOrder = function (booking) {

        bootbox.confirm("Do you wan't to make the order?", function (answer) {

            if (answer === true) {

                $scope.order = new MyBookings();
                $scope.order.start_time = booking.time_start;
                $scope.order.end_time = booking.time_end;
                $scope.order.start_date = $scope.selectedDate;
                $scope.order.user = $scope.user.id;
                $scope.order.swim_lane = 2;

                $scope.order.$save(function (response) {

                    bootbox.alert('Approved');
                    booking.is_booked = true;

                }, function (error) {

                    $scope.itemInCartError = error.data.detail;
                    Flash.create('warning', $scope.itemInCartError, 'flash-message-item-list');

                });
            }

        });


    };

    $scope.authenticate = function(provider) {
        $auth.authenticate(provider);
    };
}


angular
    .module('myApp')
    .controller('LoginCtrl', LoginCtrl);

function LoginCtrl($scope, $http, $location, $window, Flash) {

    $scope.page = '/rest-auth/login/';
    $scope.errorLoginMessage = 'Incorrect username or password.';
    $scope.loginProcess = false;

    $scope.user = {
        username : undefined,
        password: undefined
    };

    $scope.sendLoginData = function () {
        $scope.loginProcess = true;

        $http.post($scope.page, $scope.user).success(function () {

            //$location.path('/');
            $window.location.href = '/';

        }).error(function (error) {

            $scope.sendLoginDataError = error;
            Flash.create('danger', $scope.errorLoginMessage, 'flash-message');
            $scope.loginProcess = false;
        });
    };



}

angular
    .module('myApp')
    .controller('RegistrationController', RegistrationController);

function RegistrationController($scope, $http, $location, $window, Flash) {

    $scope.page = '/rest-auth/registration/';
    $scope.errorRegisterMessage = 'Incorrect username or password.';

    $scope.user = {
        username : undefined,
        password1: undefined,
        password2: undefined
    };

    $scope.sendRegisterData = function () {

        $http.post($scope.page, $scope.user).success(function () {

            //$location.path('/');
            //$window.location.href = '/';

        }).error(function (error) {

            $scope.sendRegisterDataError = error;
            Flash.create('danger', $scope.sendRegisterDataError, 'flash-message');
        });
    };

}


angular
    .module('myApp')
    .controller('BookingsController', BookingsController);

function BookingsController($scope, $http, $location, $window, Flash, MyBookings) {

    var date = new Date();
    $scope.currentDate = moment(date).format('MMMM ' + 'YYYY');
    $scope.ordersLoad = false;

    $scope.bookings = MyBookings.query(function () {

        $scope.ordersLoad = true;

    }, function () {
        $scope.bookingsLoadError = true;
    });

    $scope.removeOrder = function (index) {

        bootbox.confirm('Are you sure you want to delete this order?', function (answer) {

            if (answer === true) {
                MyBookings.delete({id: $scope.bookings[index].id}, function () {

                    $scope.bookings.splice(index, 1);

                });
            }


        });

    };


}

/**
 * Directive for formatting date from datepicker Angular UI( add action form )
 */
angular
    .module('myApp')
    .directive('myDate', function (dateFilter, $parse) {
        return {
            restrict: 'EAC',
            require: '?ngModel',
            link: function (scope, element, attrs, ngModel, ctrl) {
                ngModel.$parsers.push(function (viewValue) {
                    return dateFilter(viewValue, 'yyyy-MM-dd');
                });
            }
        }
    });

/**
 * Filter for pagination comments
 */
angular
    .module('myApp')
    .filter('startFrom', function () {
        return function (data, start) {
            if (angular.isDefined(data)) {
                return data.slice(start)
            }
        }
    });