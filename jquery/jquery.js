$.validator.setDefaults({
        submitHandler: function () {
            alert("submitted!");
        }
    });
$(document).ready(function () {
        $("#signupForm1").validate({
            rules: {
                name: "required",
                date: {
                    required: true,
                    date: true
                },
                ssn: {
                    required: true,
                    minlength: 5
                },
                address: "required",
                city: "required",
                state: "required",
                zip: {
                    required: true,
                    minlength: 5
                }
            },
            messages: {
                name: "Please enter your name",
                date: {
                    required: "Please enter a date",
                    date: "Enter a valid date."
                },
                ssn: {
                    required: "Please provide a ssn",
                    minlength: "Your ssn must be at least 5 characters long"
                },
                address: "Please provide an address",
                city: "Please provide the name of city",
                state: "Please provide the name of state",
                zip: {
                    required: "Please provide a zip",
                    minlength: "Your zip must be at least 5 characters long",
                }
            },
            errorElement: "em",
            errorPlacement: function (error, element) {
                // Add the `help-block` class to the error element
                error.addClass("help-block");

                // Add `has-feedback` class to the parent div.form-group
                // in order to add icons to inputs
                element.parents(".col-sm-5").addClass("has-feedback");

                if (element.prop("type") === "checkbox") {
                    error.insertAfter(element.parent("label"));
                } else {
                    error.insertAfter(element);
                }

                // Add the span element, if doesn't exists, and apply the icon classes to it.
                if (!element.next("span")[0]) {
                    $("<span class='glyphicon glyphicon-remove form-control-feedback'></span>").insertAfter(element);
                }
            },
            success: function (label, element) {
                // Add the span element, if doesn't exists, and apply the icon classes to it.
                if (!$(element).next("span")[0]) {
                    $("<span class='glyphicon glyphicon-ok form-control-feedback'></span>").insertAfter($(element));
                }
            },
            highlight: function (element, errorClass, validClass) {
                $(element).parents(".col-sm-5").addClass("has-error").removeClass("has-success");
                $(element).next("span").addClass("glyphicon-remove").removeClass("glyphicon-ok");
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).parents(".col-sm-5").addClass("has-success").removeClass("has-error");
                $(element).next("span").addClass("glyphicon-ok").removeClass("glyphicon-remove");
            }
        });
    });