# Message Queue System

This project implements a message queue system using a producer Lambda function and two consumer Lambda functions, all connected via Amazon SQS (FIFO).

![Architecture Diagram](https://github.com/user-attachments/assets/70e0da4e-35bd-4114-9901-6f0e44031256)

## AWS Roles

A role was created that provides full access to CloudWatch and SQS.

![Roles Configuration](https://github.com/user-attachments/assets/17d2b826-a6db-45be-8ae4-7710862c2544)

## SQS Configuration

An SQS FIFO queue was created to facilitate message processing.

![SQS Setup](https://github.com/user-attachments/assets/8d7b315c-6df1-459c-afe5-0840c1068993)

## Lambda Functions

Three Lambda functions were created for this system:

1. **Producer Lambda**
   ![Producer Function](https://github.com/user-attachments/assets/f54b6e38-5518-4fae-9490-ffb63c185315)

2. **Consumer Lambda #1**
   ![Consumer Function #1](https://github.com/user-attachments/assets/17b54c81-129a-4fe8-800c-4b1d15149811)

3. **Consumer Lambda #2**
   ![Consumer Function #2](https://github.com/user-attachments/assets/ff43584d-efba-4007-a517-dc5ac7f6ab3a)

## Testing

The system was tested successfully, and the following results were observed:

![Testing Overview](https://github.com/user-attachments/assets/b4efd5a3-61b1-4e0e-81d7-5bc0e19489df)

### Test Results

- **Test Success**
  ![Test Success](https://github.com/user-attachments/assets/db699668-f79e-4c74-980a-887244adace7)

- **SQS Message Queue Status**
  - Messages in flight: 20 (Current message count: 70)
    ![SQS Message Queue Filled](https://github.com/user-attachments/assets/0236a1ec-bee6-46e3-81ed-a8ffad06d130)
  - Messages in flight: 20 (Current message count: 40)
    ![SQS Message Queue Filled - State 2](https://github.com/user-attachments/assets/01666c57-32c8-4fea-8b95-e21d8585a847)
  - Messages in flight: 0 (Current message count: 0)
    ![SQS Message Queue Empty](https://github.com/user-attachments/assets/025b9005-77a8-4134-9a17-3308464cae7c)

## Logs

### Producer Logs
![Producer Logs](https://github.com/user-attachments/assets/06e55c9a-8ec6-43b5-9d53-b630f2c25b4d)

### Consumer #1 Logs
![Consumer #1 Logs](https://github.com/user-attachments/assets/3915d847-347c-4e57-b68d-51cbf15f8049)

### Consumer #2 Logs
![Consumer #2 Logs](https://github.com/user-attachments/assets/a4ae372b-83a7-4bc8-9214-152283d47ab9)
