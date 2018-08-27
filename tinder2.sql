-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2018 at 09:02 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tinder2`
--

-- --------------------------------------------------------

--
-- Table structure for table `proposals`
--

CREATE TABLE `proposals` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proposals`
--

INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(3, 6, 4),
(4, 8, 9),
(5, 8, 6),
(6, 9, 4),
(7, 9, 8),
(8, 9, 3),
(9, 4, 9),
(11, 4, 12),
(12, 12, 13),
(13, 15, 17),
(14, 23, 12),
(15, 6, 7),
(16, 15, 1),
(17, 4, 6),
(18, 15, 26),
(19, 27, 12);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `city` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `age`, `city`) VALUES
(4, 'Spandan Guha', 'princy.guha99@gmail.com', '12345', 'Male', 21, 'Kolkata'),
(6, ' Disha Dutta', 'dishadutta@gmail.com', '123456', ' female', 18, ' bhuvaneshwar'),
(7, 'Deborshi Das', 'deborshi@gmail.com', '123456', 'male', 21, 'srirampur'),
(8, 'debarghya dutta', 'redjohnshelby@gmail.com', '12345', 'male', 21, 'burdwan'),
(9, 'nasrin naz', 'nasrinnaz@gmail.com', '12345', 'female', 21, 'malda'),
(12, 'Lionel Messi', 'lionelmessi@gmail.com', '12345', 'male', 31, 'Barcelona'),
(13, 'Cristiano Ronaldo', 'cr7@gmail.com', '12345', 'male', 33, 'Juventus'),
(15, 'a', 'a', '1', 'm', 1, 'x'),
(23, 'sohini dasgupta', 'sohini@gmail.com', '123456', 'female', 21, 'dumdum'),
(25, 'amrita de', 'amrita@gmail.com', '123456', 'female', 21, 'seoraphuli'),
(26, 'poulomi sen', 'poulomi@gmail.com', '123456', 'female', 21, 'srerampore'),
(27, 'bhaskar banerjee', 'bhaskar@gmail.com', '12345', 'male', 50, 'srerampore');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposals`
--
ALTER TABLE `proposals`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposals`
--
ALTER TABLE `proposals`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
