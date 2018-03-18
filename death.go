package main
import (
  "log"
  "os"
  "github.com/dotabuff/manta"
  "github.com/dotabuff/manta/dota"
  //"io/ioutil"
)

func main() {
  // Create a new parser instance from a file. Alternatively see NewParser([]byte)

  f, err := os.Open("3594879358.dem")
  if err != nil {
    log.Fatalf("unable to open file: %s", err)
  }
  defer f.Close()

  p, err := manta.NewStreamParser(f)
  if err != nil {
    log.Fatalf("unable to create parser: %s", err)
  }
  //func (c *Callbacks) OnCDOTAUserMsg_CombatLogShowDeath(fn func(*dota.CDOTAUserMsg_CombatLogShowDeath) error)
  //func (c *Callbacks) OnCDOTAUserMsg_KillcamDamageTaken(fn func(*dota.CDOTAUserMsg_KillcamDamageTaken) error)
/*p.Callbacks.OnCDOTAUserMsg_CombatLogShowDeath(func(m *dota.CDOTAUserMsg_CombatLogShowDeath) error {
    log.Printf("%s", m)
   return nil
  })*/




  p.Callbacks.OnCMsgDOTACombatLogEntry(func(m *dota.CMsgDOTACombatLogEntry) error {
    log.Printf("%s", m)
   //ioutil.WriteFile("output.txt", m, 0644)
   return nil
  })

  // Start parsing the replay!
  p.Start()
  //log.Printf("Parse Complete!\n")
}