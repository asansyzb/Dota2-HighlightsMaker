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

  f, err := os.Open("3525840237.dem")
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

    t := m.GetType()
    switch dota.DOTA_COMBATLOG_TYPES(t) {
      /*case dota.DOTA_COMBATLOG_TYPES_DOTA_COMBATLOG_XP:
            amount := m.GetValue()
            reason := m.GetXpReason() 
            //"0": "Other", "1": "Hero", "2": "Creep", "3": "Roshan"
                    
            target, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetTargetName()))
            log.Printf("{\"target\":\"%s\",\"reason\":%d,\"amount\":%d, \"whole Log\": %s}", target, reason, amount, m)     */ 
            //log.Printf("%s", m)
      case dota.DOTA_COMBATLOG_TYPES_DOTA_COMBATLOG_DAMAGE:
              /*iat := m.GetIsAttackerIllusion()
              iah := m.GetIsAttackerHero()
              iti := m.GetIsTargetIllusion()
              ith := m.GetIsTargetHero()
              ivr := m.GetIsVisibleRadiant()
              ivd := m.GetIsVisibleDire()
              itb:= m.GetIsTargetBuilding()*/
              
              target, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetTargetName()))
              targetSource, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetTargetSourceName()))
              attacker, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetAttackerName()))
              damageSource, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetDamageSourceName())) 
              inflictor, _ := p.LookupStringByIndex("CombatLogNames", int32(m.GetInflictorName()))
              value := m.GetValue()
              log.Printf("\"target\":\"%s\" \"targetSource\":%s \"attacker\":%s  \"damageSource\": %s \"inflictor\":%s \"value\": %d %s", 
                target, targetSource, attacker, damageSource, inflictor, value, m)  
      //ioutil.WriteFile("output.txt", m, 0644)
    }
    return nil
  })

  // Start parsing the replay!
  p.Start()
  //log.Printf("Parse Complete!\n")
}