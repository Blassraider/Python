import time
import random
from threading import Thread, current_thread, Condition
 
'''
# TODO Explain what is condition used for?
# A Condition object that acts like a lock on the shared resource (the log buffer).
# It ensures that only one thread (either the LogGenerator or LogArchiver) can
# access the buffer at a time. It also provides wait() and notify() so threads
# can signal each other in which the generator notifies the archiver when a new log is
# ready, and the archiver notifies the generator when the buffer is empty and
# ready for the next log. Without this coordination, both threads could access
# the buffer simultaneously, causing data loss or incorrect behavior.
 
# TODO Explain how does is_empty maintain the state management?
# is_empty is a Boolean flag that tracks whether the buffer currently holds an
# unprocessed log entry. It starts as True (buffer is empty, ready to write).
# When the LogGenerator writes a log, it sets is_empty = False, signaling that
# the buffer is full and the archiver should process it. When the LogArchiver
# processes the log, it sets is_empty = True, signaling that the buffer is clear
# and the generator can write the next log. Each thread checks this flag inside
# a while loop with wait() to avoid proceeding at the wrong time.
'''
 
class LogBuffer:
    def __init__(self):
        self.current_log = None
        self.is_empty = True
        self.condition = Condition()
 
    def write_log(self, log_msg):
        # TODO: Acquire the condition lock, wait if buffer is not empty,
        # write the log, set is_empty to False, and then notify the archiver.
        with self.condition:
            while not self.is_empty:
                print("[Generator] Buffer is full, waiting for archiver...")
                self.condition.wait()
            self.current_log = log_msg
            self.is_empty = False
            print(f"[Generator] Wrote log     --> {self.current_log}")
            self.condition.notify()
 
    def archive_log(self):
        # TODO: Acquire the condition lock, wait if buffer is empty,
        # read/process the log, set is_empty to True, and then notify the generator.
        with self.condition:
            while self.is_empty:
                print("[Archiver]  Buffer is empty, waiting for generator...")
                self.condition.wait()
            log = self.current_log
            self.current_log = None
            self.is_empty = True
            print(f"[Archiver]  Archived log  --> {log}")
            self.condition.notify()
            return log
 
 
class LogGenerator(Thread):
    # TODO: Define __init__ and the run methods.
    # __init__ should accept the shared buffer and log count.
    # Then, run should generate LOG_COUNT log entries and write each to the buffer.
    def __init__(self, buffer, log_count):
        super().__init__()
        self.buffer = buffer
        self.log_count = log_count
 
    def run(self):
        services = ["AuthService", "DatabaseService", "WebServer", "CacheService", "SchedulerService"]
        levels   = ["INFO", "WARNING", "ERROR", "DEBUG"]
        for i in range(1, self.log_count + 1):
            time.sleep(random.uniform(0.1, 0.5))   
            service = random.choice(services)
            level   = random.choice(levels)
            msg = f"[{level}] {service}: Log entry #{i}"
            self.buffer.write_log(msg)
        print("[Generator] Finished generating all logs.")
 
 
class LogArchiver(Thread):
    # TODO: Define __init__ and run methods.
    # __init__ should accept the shared buffer and log count.
    # Then, run should archive LOG_COUNT log entries from the buffer.
    def __init__(self, buffer, log_count):
        super().__init__()
        self.buffer = buffer
        self.log_count = log_count
 
    def run(self):
        for i in range(1, self.log_count + 1):
            time.sleep(random.uniform(0.1, 0.4))   
            log = self.buffer.archive_log()
            print(f"[Archiver]  Processing complete for entry #{i}")
        print("[Archiver]  Finished archiving all logs.")
 
 
def main():
    LOG_COUNT = 5
    buffer = LogBuffer()
    
    gen = LogGenerator(buffer, LOG_COUNT)
    arc = LogArchiver(buffer, LOG_COUNT)
    
    gen.start()
    arc.start()
    
    gen.join()
    arc.join()
    print("\nLog Maintenance Complete.")
 
if __name__ == "__main__":
    main()
