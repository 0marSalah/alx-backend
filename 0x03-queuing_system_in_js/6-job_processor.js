#!/usr/bin/node
import kue from "kue";

const queue = kue.createQueue();

/**
 * Process a job
 * @param {String} phoneNumber 
 * @param {String} message 
 */
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

queue.process("push_notification_code", (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});
