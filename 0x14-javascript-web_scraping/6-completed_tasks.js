#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId]++;
      }
    }
  });

  Object.keys(completedTasks).forEach(userId => {
    console.log(`{ ${userId}: ${completedTasks[userId]}}`);
  });
});
