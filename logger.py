import logging
from datetime import datetime
import os
import sys

class RoomLogger:
    @staticmethod
    def setup_logger(room_name: str) -> logging.Logger:
        # Create logs directory if not exists
        logs_dir = "chat_logs"
        os.makedirs(logs_dir, exist_ok=True)
        
        # Create unique log file name with process id
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pid = os.getpid()
        log_file = os.path.join(logs_dir, f"{room_name}_pid{pid}_{timestamp}.log")
        
        # Get logger
        logger = logging.getLogger(f"{room_name}_{pid}")  # Unique logger name per process
        if logger.handlers:  # Clear any existing handlers
            logger.handlers.clear()
        
        logger.setLevel(logging.INFO)
        
        # Add handlers
        file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
        console_handler = logging.StreamHandler(sys.stdout)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.propagate = False
        
        return logger
