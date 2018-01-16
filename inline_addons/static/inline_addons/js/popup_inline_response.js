/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.dismissChangeInlineObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.dismissDeleteInlineObjectPopup(window, initData.value);
        break;
    default:
        opener.dismissAddInlineObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();
