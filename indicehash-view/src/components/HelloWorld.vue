<template>
  <!-- 
    Colors:
    - P   = #00bcd4   (D)
    - PC  = #6ff9ff   (D)
    - PD  = #0095a8   (l)
    - S   = #ffa726   (l)
    - SC  = #ffd95b   (l)
    - SD  = #c77800   (l)
   -->
  <v-container>
    <div v-if="isInit">
      <v-spacer></v-spacer>
      <v-card color="#00bcd4" dark outlined tile>
        <v-card-title>TESTE</v-card-title>

        <v-divider class="mx-4"></v-divider>

        <v-row class="ma-4">  
          <v-text-field 
          label="Pesquisar por..."
          outlined
          clearable
          prepend-inner-icon="mdi-magnify">

          </v-text-field>
        </v-row>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="#0095a8">Pesquisar</v-btn>
        </v-card-actions>
      </v-card>

      <v-card v-if="isResponseAvailable" color="#00bcd4" dark outlined tile>
        <p class="ma-4  ">TESTE</p>
      </v-card>
      <v-spacer></v-spacer>

    </div>
    <div v-else aria-colcount="">
        
    </div>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data() {
    return {
      isInit: true,
      isResponseAvailable: false
    }
  },
};
</script>
