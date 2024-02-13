#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  let a = 0;
  while ((l - a) > 0) {
    const aux = list[l];
    list[l] = list[a];
    list[a] = aux;
    a++;
    l--;
  }
  return list;
};
