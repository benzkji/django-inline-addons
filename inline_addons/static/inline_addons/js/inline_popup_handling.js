/*global SelectBox, interpolate*/
// Handles inline-objects functionality: lookup link for raw_id_fields
// and Add Another links.

// modified for use with inline popups by django-inline-addons

(function($) {
    'use strict';

    function dismissAddInlineObjectPopup(win, newId, newRepr) {
        var id = windowname_to_id(win.name);
        var input = $('#' + id);
        var text = $('#' + id + "_textual");
        input.val(newId);
        text.html(newRepr);
        // modify management form, to prevent a double save
        var prefix = input.closest('.popup-inline-group').attr('data-prefix');
        var selector = '#id_' + prefix + '-INITIAL_FORMS';
        var initial_forms = $(selector);
        initial_forms.val(parseInt(initial_forms.val()) + 1);
        win.close();
    }

    function dismissChangeInlineObjectPopup(win, objId, newRepr, newId) {
        var id = windowname_to_id(win.name).replace(/^edit_/, '');
        var input = $('#' + id);
        var text = $('#' + id + "_textual");
        input.val(newId);
        text.html(newRepr);
        win.close();
    }

    // probably never used with popuo inlines!?
    function dismissDeleteInlineObjectPopup(win, objId) {
        alert('dismissDeleteInlineObjectPopup not implemented!');
    }

    // Globals, for when coming back
    window.dismissAddInlineObjectPopup = dismissAddInlineObjectPopup;
    window.dismissChangeInlineObjectPopup = dismissChangeInlineObjectPopup;
    window.dismissDeleteInlineObjectPopup = dismissDeleteInlineObjectPopup;

    $(document).ready(function() {
        // fetch the add!
        $(document).on('formset:added', function(event, $row, formsetName) {
            if ($row.hasClass('popup-inline')) {
                // trigger popup
                $row.find('.inlinechangelink')[0].click();
            }
        });
    });

})(django.jQuery);
