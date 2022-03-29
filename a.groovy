xlr {
  template('test-script') {
    folder('yoo')
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2022-03-28T09:00:00-0400')
    scriptUsername 'admin'
    scriptUserPassword '{aes:v0}sL5f2P7N8TjKKfZbcmFnmrDnVFLwj5GsexnlSREERYg='
    phases {
      phase('ph1') {
        color '#3d6c9e'
        tasks {
          script('2') {
            script (['''\
print "hello"
'''])
          }
        }
      }
    }
    
  }
}