#!/usr/bin/node
import kue from "kue";

const queue = kue.createQueue();

const blackList = ["4153518780", "4153518781"];

/**
 * Process a job
 * @param {String} phoneNumber
 * @param {String} message
 * @param {Obj} job
 * @param {Function} done
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blackList.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);

  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
  setTimeout(() => {
    done();
  }, 1000);
};

queue.process("push_notification_code", (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
