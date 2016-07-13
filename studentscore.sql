-- MySQL dump 10.13  Distrib 5.7.13, for Win64 (x86_64)
--
-- Host: localhost    Database: studentscore
-- ------------------------------------------------------
-- Server version	5.7.13-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `studentscore`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `studentscore` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `studentscore`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add class',6,'add_class'),(17,'Can change class',6,'change_class'),(18,'Can delete class',6,'delete_class'),(19,'Can add course',7,'add_course'),(20,'Can change course',7,'change_course'),(21,'Can delete course',7,'delete_course'),(22,'Can add person',8,'add_person'),(23,'Can change person',8,'change_person'),(24,'Can delete person',8,'delete_person'),(25,'Can add score',9,'add_score'),(26,'Can change score',9,'change_score'),(27,'Can delete score',9,'delete_score');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classinfo`
--

DROP TABLE IF EXISTS `classinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classid` varchar(16) NOT NULL,
  `classname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `classid` (`classid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classinfo`
--

LOCK TABLES `classinfo` WRITE;
/*!40000 ALTER TABLE `classinfo` DISABLE KEYS */;
INSERT INTO `classinfo` VALUES (1,'2013211309','计科9班'),(2,'2013211303','计科3班');
/*!40000 ALTER TABLE `classinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courseinfo`
--

DROP TABLE IF EXISTS `courseinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `courseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `begindate` date NOT NULL,
  `enddate` date NOT NULL,
  `term` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courseinfo`
--

LOCK TABLES `courseinfo` WRITE;
/*!40000 ALTER TABLE `courseinfo` DISABLE KEYS */;
INSERT INTO `courseinfo` VALUES (1,'2016-03-01','2016-06-30','2016年春','数据库概念');
/*!40000 ALTER TABLE `courseinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Person_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Person_id` FOREIGN KEY (`user_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'UserMgr','class'),(7,'UserMgr','course'),(8,'UserMgr','person'),(9,'UserMgr','score');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'UserMgr','0001_initial','2016-07-12 23:59:29.000000'),(2,'UserMgr','0002_auto_20160713_0758','2016-07-12 23:59:29.000000'),(3,'contenttypes','0001_initial','2016-07-12 23:59:29.000000'),(4,'admin','0001_initial','2016-07-12 23:59:31.000000'),(5,'admin','0002_logentry_remove_auto_add','2016-07-12 23:59:31.000000'),(6,'contenttypes','0002_remove_content_type_name','2016-07-12 23:59:32.000000'),(7,'auth','0001_initial','2016-07-12 23:59:36.000000'),(8,'auth','0002_alter_permission_name_max_length','2016-07-12 23:59:37.000000'),(9,'auth','0003_alter_user_email_max_length','2016-07-12 23:59:37.000000'),(10,'auth','0004_alter_user_username_opts','2016-07-12 23:59:37.000000'),(11,'auth','0005_alter_user_last_login_null','2016-07-12 23:59:37.000000'),(12,'auth','0006_require_contenttypes_0002','2016-07-12 23:59:37.000000'),(13,'auth','0007_alter_validators_add_error_messages','2016-07-12 23:59:37.000000'),(14,'sessions','0001_initial','2016-07-12 23:59:38.000000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ire2fk1vde0j9ksn4ta14ht1om8vmq5q','YzQ0NjY1ZjAxZjQ5YTFmM2MzZDQxMTY1ZDZjYmQzZmE4N2E0ZTE2MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjQzNDgzYzA5M2Q5MzgwODU0Y2U5NzgzODFhODg0MGEzYzA5ODIxZGEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2016-07-27 04:26:31');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `username` varchar(40) NOT NULL,
  `role` int(11) NOT NULL,
  `realname` varchar(16) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `theclass_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `Person_theclass_id_987a41c9_fk_ClassInfo_id` (`theclass_id`),
  CONSTRAINT `Person_theclass_id_987a41c9_fk_ClassInfo_id` FOREIGN KEY (`theclass_id`) REFERENCES `classinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'pbkdf2_sha256$24000$AG21jBhpxVJi$in8wDBeytOM15fm88sse/BXAxBBLShM1E3LPvgJfc3k=','2016-07-13 04:24:08','admin',2,'','',NULL),(2,'pbkdf2_sha256$24000$3Uo8TesTOJgG$Bho/4zriBm2TmBHLfuuSXkweJG0Z83sbrjSYy04Jgko=','2016-07-13 04:24:26','2013211277',1,'阳光','1',NULL),(3,'pbkdf2_sha256$24000$6GVHMaxpCSHp$9w8W6LbrW8I6tHkmgpheeWdKWHQAwgxJ7Yy50+iJhxA=','2016-07-13 10:48:25','2013211412',0,'灰灰','0',1),(4,'pbkdf2_sha256$24000$YKVl08bGYQj4$xPxnFU5e0Zw3zBc2WZrf1GslM1/irRz4LYzC995ws90=','2016-07-13 10:51:18','2013211414',0,'傻逼峰','0',1),(5,'pbkdf2_sha256$24000$4pXzw21HoGX1$LjTAs/63Uxu4doMZrvZWKexe/ksTmPWFpEGRlMkoJTM=','2016-07-13 04:26:31','2013211228',0,'苏璟','0',2);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person_course`
--

DROP TABLE IF EXISTS `person_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Person_course_person_id_0e3848dc_uniq` (`person_id`,`course_id`),
  KEY `Person_course_course_id_28bd3a3a_fk_CourseInfo_id` (`course_id`),
  CONSTRAINT `Person_course_course_id_28bd3a3a_fk_CourseInfo_id` FOREIGN KEY (`course_id`) REFERENCES `courseinfo` (`id`),
  CONSTRAINT `Person_course_person_id_103db5b2_fk_Person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person_course`
--

LOCK TABLES `person_course` WRITE;
/*!40000 ALTER TABLE `person_course` DISABLE KEYS */;
INSERT INTO `person_course` VALUES (1,2,1);
/*!40000 ALTER TABLE `person_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usermgr_score`
--

DROP TABLE IF EXISTS `usermgr_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usermgr_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UserMgr_score_course_id_e6e8046d_fk_CourseInfo_id` (`course_id`),
  KEY `UserMgr_score_30a811f6` (`student_id`),
  CONSTRAINT `UserMgr_score_course_id_e6e8046d_fk_CourseInfo_id` FOREIGN KEY (`course_id`) REFERENCES `courseinfo` (`id`),
  CONSTRAINT `UserMgr_score_student_id_d4e34486_fk_Person_id` FOREIGN KEY (`student_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermgr_score`
--

LOCK TABLES `usermgr_score` WRITE;
/*!40000 ALTER TABLE `usermgr_score` DISABLE KEYS */;
INSERT INTO `usermgr_score` VALUES (1,88,1,5),(2,90,1,3),(3,99,1,4);
/*!40000 ALTER TABLE `usermgr_score` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-13 19:33:54
