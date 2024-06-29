#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  let userIds = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!userIds[todo.userId]) {
        userIds[todo.userId] = 0;
      }
      userIds[todo.userId]++;
    }
  });

  console.log(userIds);
});


