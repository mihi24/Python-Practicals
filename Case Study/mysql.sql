CREATE SCHEMA `mysql` ;

CREATE TABLE `pysql`.`studentinf` (
  `PrnNo` INT NOT NULL,
  `firstName` VARCHAR(45) NOT NULL,
  `MiddleName` VARCHAR(45) NOT NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `mobileNo` VARCHAR(45) NOT NULL,
  `emailId` VARCHAR(45) NOT NULL,
  `dob` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PrnNo`));

INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2011', 'Pratik', 'Raj', 'Jain', 'Pune', '978785656', 'PJ@gmail.com', '22/9/2003');
INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2012', 'Rajan', 'Aman', 'Mahajan', 'Delhi', '9967565589', 'Raja@gmail.com', '17/12/2002');
INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2013', 'Rajvi', 'Raja', 'Patil', 'Siliguri', '72745390836', 'Rjaph@gmail.com', '31/12/2001');
INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2014', 'akshay', 'Vijay', 'Joshi', 'Chennai', '8945896732', 'akshay@gmail.com', '2/7/2002');
INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2015', 'Nilanshi', 'Prakash', 'Patel', 'Kota', '9856763421', 'Patel@gmail.com', '9/6/2002');
INSERT INTO `pysql`.`studentinf` (`PrnNo`, `firstName`, `MiddleName`, `lastName`, `address`, `mobileNo`, `emailId`, `dob`) VALUES ('2016', 'Mansi', 'Sanjay', 'Patil', 'Ludhiana', '7856894523', 'mansi@gmail.com', '19/4/2002');
