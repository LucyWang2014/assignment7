'''import all modules for assignment7'''

import Problem1, Problem2, Problem3, Problem4

'''main function calls all modules'''
def main():
  print "=======================Problem 1========================="
  Problem1.main()
  print "=======================Problem 2========================="
  Problem2.main()
  print "=======================Problem 3========================="
  Problem3.main()
  print "=======================Problem 4========================="
  Problem4.main()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
