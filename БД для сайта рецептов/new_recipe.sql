-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: recipes
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `id_recipe` int NOT NULL AUTO_INCREMENT,
  `name_recipe` varchar(255) NOT NULL,
  `recipe` longtext NOT NULL,
  `id_user` int NOT NULL,
  `description` varchar(250) NOT NULL,
  `recipe_photo` varchar(255) DEFAULT NULL,
  `category` varchar(45) NOT NULL,
  PRIMARY KEY (`id_recipe`),
  KEY `id_user_idx` (`id_user`),
  CONSTRAINT `id_user` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'Карбонара','Берем макарохи, варим макарохи. Берем бекон, жарим бекон, добавляем сливки и тушим. Добавляем чуть недоваренные макарохи. Доводим до готовности, накладываем в тарелочки и кайфуем!',1,'Самая вкусная паста с беконом',NULL,'Вторые'),(2,'Мясное рагу','Подготавливаем все необходимые продукты. Ещё понадобится 200 мл горячей воды. Лук очищаем и нарезаем полукольцами. В казане, толстостенной кастрюле или глубокой сковороде разогреваем растительное масло и обжариваем лук на среднем огне 3-5 минут, до мягкости и золотистого оттенка. Морковь очищаем, нарезаем брусочками и добавляем к луку. Перемешиваем, накрываем крышкой и на минимальном огне готовим 3-4 минуты. Свинину нарезаем небольшими брусочками и добавляем к овощам.',1,'Яркое ассорти из овощей с мясом. Свинина сперва обжаривается с луком и морковью, а затем тушится с тыквой, картофелем, кабачком и сладким перцем. Готовится рагу в одной посуде, получается сочным и очень ароматным.',NULL,'Вторые'),(3,'Борщ','Берем ингредиенты: свеклу, картоху, лук и какое-нибудь мясо, чтобы было вкуснее.\r\nСтавим вариться свеклу, и в это время варим мясной бульон.\r\nКогда свекла сварилась, остужаем ее до комнатной температуры.\r\nНарезаем все остальные ингредиенты по своему усмотрению, но чтобы были не слишком крупные, а то долго будем варить.\r\nСвеклу натираем на терке.\r\nНарезанное кидаем и варим до полной готовности.\r\nПосле варения добавляем свеклу и включаем пожарную сигнализацию, чтобы все соседи узнали, что вы приготовили борщ.\r\nГотово!!',8,'Самый вкусный борщ, на который сбегутся все соседи!',NULL,'Супы'),(8,'Борщ-2','Берем ингредиенты: свеклу, картоху, лук и какое-нибудь мясо, чтобы было вкуснее.\r<br />Ставим вариться свеклу, и в это время варим мясной бульон.\r<br />Когда свекла сварилась, остужаем ее до комнатной температуры.\r<br />Нарезаем все остальные ингредиенты по своему усмотрению, но чтобы были не слишком крупные, а то долго будем варить.\r<br />Свеклу натираем на терке.\r<br />Нарезанное кидаем и варим до полной готовности.\r<br />После варения добавляем свеклу и включаем пожарную сигнализацию, чтобы все соседи узнали, что вы приготовили борщ.\r<br />Готово!!',8,'Самый вкусный борщ, на который сбегутся все соседи!','борщец.jpg','Супы'),(13,'Тёртый пирог с цедрой апельсина и шоколадным заварным кремом','Подготовить необходимые продукты.<br />Для приготовления теста в глубокой ёмкости соединить яйцо, сахар и соль. При помощи венчика перемешать массу до растворения ингредиентов.<br />Тем временем с апельсина снять цедру.<br />В яичную массу всыпать 1,5 ч. ложки апельсиновой цедры.<br />В кастрюле на небольшом огне растопить сливочное масло. Остудить.<br />Влить сливочное масло в яичную смесь, перемешать.<br />Всыпать муку и разрыхлитель.<br />Руками замесить пластичное тесто.<br />Подкатать тесто в шар и разделить на 2 неравные части. Меньшую часть теста завернуть в пищевую плёнку и отправить в морозильную камеру.<br />Дно формы (моя - диаметром 20 см) застелить пергаментом и выложить туда бóльшую часть теста. Распределить тесто по дну и бортикам. Бортики должны получиться не менее 6 сантиметров высотой.<br />Вилкой наколоть тесто - и бортики, и дно.<br />Тесто с формой отправить в холодильник.<br />В сотейник с толстым дном влить 1/3 молока. Добавить яйца и сахар.<br />Всыпать ванильный сахар и кукурузный крахмал.<br />Также добавить какао-порошок.<br />При помощи венчика аккуратно перемешать массу до полного растворения комочков.<br />Варить 8-10 минут на среднем огне, помешивая.<br />Когда масса загустеет - снять сотейник с огня. Затем ещё 2 минуты перемешивать массу.<br />Выложить крем на тесто в форме, поверхность разровнять. Бортики из теста должны быть выше уровня крема на 0,5 см.<br />Меньшую часть теста вынуть из морозильной камеры и натереть на крупной тёрке, распределяя поверх крема.<br />Таким образом закрыть весь крем равномерным слоем тёртого теста.<br />Форму отправить в разогретую духовку, выпекать пирог при 180 градусах 40 минут, до появления румяной корочки.<br />По истечении времени пирог вынуть из духовки и остудить, чтобы крем стабилизировался.<br />Готовый пирог извлечь из формы, выложить на блюдо и украсить на своё усмотрение.<br />Тёртый пирог с цедрой апельсина и шоколадным заварным кремом готов к подаче.<br />Приятного аппетита!',2,'Ароматный тёртый пирог с восхитительным вкусом. Тесто замешивается на основе сливочного масла и яйца, с добавлением разрыхлителя и апельсиновой цедры. Достаточное количество шоколадной начинки обеспечивает выпечке насыщенный вкус.','big_688403.jpg','Выпечка');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id_role` int NOT NULL AUTO_INCREMENT,
  `name_role` varchar(45) NOT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'user'),(2,'admin'),(3,'пук'),(4,'пик'),(5,'asdasfas');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id_role` int NOT NULL AUTO_INCREMENT,
  `name_role` varchar(45) NOT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'user'),(2,'admin'),(5,'пук'),(6,'тук'),(7,'би-би');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `role` int NOT NULL,
  `user_info` varchar(255) DEFAULT NULL,
  `user_photo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  KEY `role_idx` (`role`),
  CONSTRAINT `role` FOREIGN KEY (`role`) REFERENCES `role` (`id_role`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'sonya','s@mail.ru','1111',1,'Красивая девчуля и милая котюля','sonya.jpg'),(2,'serg','s@gmail.com','2222',2,'Я не сплю...','ава.jpg'),(5,'aa','aa@aa','1',1,NULL,NULL),(7,'bb','bb@bb','2',1,NULL,NULL),(8,'a','aa@aa.ru','a',1,'Стала a','a.jpg'),(9,'lexa','bfussfdgvb@vhcisodf','3',1,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-12  6:30:22
