USE desk_management;
-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 12, 2025 at 06:52 AM
-- Server version: 8.0.41-0ubuntu0.24.10.1
-- PHP Version: 8.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `desk_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `desks`
--

CREATE TABLE `desks` (
  `desk_id` varchar(50) NOT NULL,
  `vergesense_area_id` varchar(50) DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `desks`
--

INSERT INTO `desks` (`desk_id`, `vergesense_area_id`, `notes`, `created_at`) VALUES
('D-101', 'A-5001', 'Near window, east wing', '2025-05-12 06:18:01'),
('D-102', 'A-5001', 'Adjacent to D-101', '2025-05-12 06:18:01'),
('D-201', 'A-5002', 'Standing desk zone', '2025-05-12 06:18:01'),
('D-202', 'A-5002', 'Standing desk, corner spot', '2025-05-12 06:18:01'),
('D-301', 'A-5003', 'Quiet zone', '2025-05-12 06:18:01'),
('D-302', 'A-5004', 'Near cafeteria', '2025-05-12 06:18:01'),
('D-303', 'A-5003', 'Near cafeteria', '2025-05-12 06:18:01'),
('D-304', 'A-5003', 'Standing desk near cafeteria', '2025-05-12 06:18:01');

-- --------------------------------------------------------

--
-- Table structure for table `desk_bookings`
--

CREATE TABLE `desk_bookings` (
  `booking_id` int NOT NULL,
  `desk_id` varchar(50) DEFAULT NULL,
  `booking_date` date NOT NULL,
  `is_deleted` tinyint NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `desk_bookings`
--

INSERT INTO `desk_bookings` (`booking_id`, `desk_id`, `booking_date`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'D-201', '2025-05-12', 0, '2025-05-12 06:17:09', '2025-05-12 06:17:28'),
(2, 'D-101', '2025-05-11', 0, '2025-05-12 06:17:09', '2025-05-12 06:17:28'),
(8, 'D-201', '2025-05-13', 0, '2025-05-12 06:17:09', '2025-05-12 06:17:28'),
(10, 'D-101', '2025-05-13', 1, '2025-05-12 06:17:09', '2025-05-12 06:18:53');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `desks`
--
ALTER TABLE `desks`
  ADD PRIMARY KEY (`desk_id`);

--
-- Indexes for table `desk_bookings`
--
ALTER TABLE `desk_bookings`
  ADD PRIMARY KEY (`booking_id`),
  ADD UNIQUE KEY `desk_id` (`desk_id`,`booking_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `desk_bookings`
--
ALTER TABLE `desk_bookings`
  MODIFY `booking_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `desk_bookings`
--
ALTER TABLE `desk_bookings`
  ADD CONSTRAINT `desk_bookings_ibfk_1` FOREIGN KEY (`desk_id`) REFERENCES `desks` (`desk_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
