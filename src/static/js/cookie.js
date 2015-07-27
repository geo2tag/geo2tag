/*
= require modules
*/
/**
# Creates cookie specified by name and value
# @param {string} name: name of cookie
# @param {string} value: value of cookie
*/
var createCookie, readCookie;
createCookie = function(name, value) {
  return document.cookie = name + '=' + value + '; path=/';
};
/**
# Reads cookie specified by name
# @param {string} name: name of cookie
# @return {string} cookie value found by name
*/
readCookie = function(name) {
  if (document.cookie.indexOf(name) === -1) {
    return;
  }
  return document.cookie.split(name + '=')[1].split(';')[0];
};
window.NM.cookies = {
  createCookie: createCookie,
  readCookie: readCookie
};
