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
    <div v-if="!isInit">
      <v-spacer></v-spacer>
      <v-card color="#00bcd4" dark outlined >
        <v-card-title>TESTE</v-card-title>

        <v-divider class="mx-4"></v-divider>

        <v-row class="ma-4">
          <v-text-field
            label="Pesquisar por..."
            outlined
            clearable
            prepend-inner-icon="mdi-database-search"
          >
          </v-text-field>
        </v-row>

        <v-card-actions class="ma-4">
          <v-spacer></v-spacer>
          <v-btn color="#0095a8">Pesquisar</v-btn>
        </v-card-actions>
      </v-card>

      <v-card class="mt-2" v-if="!isResponseAvailable" color="#00bcd4" dark outlined >
        <v-card-title>TESTE</v-card-title>
      </v-card>
      <v-spacer></v-spacer>
    </div>
    <div v-else>
      <v-card color="#00bcd4" dark outlined >
        <v-card-title>Crie seu banco!</v-card-title>
        <v-divider class="mx-4"></v-divider>
        <div class="ma-4">
          <v-row class="ma-4">
            <v-text-field
              class="mr-1"
              label="Tamanho da Pagina"
              outlined
              clearable
              prepend-inner-icon="mdi-database-cog "
            >
            </v-text-field>
            <v-text-field
              class="ml-1"
              label="Tamanho do Bucket"
              outlined
              clearable
              prepend-inner-icon="mdi-database-cog "
            >
            </v-text-field>
          </v-row>
          <v-textarea class="ma-4" label="Seu texto aqui s2" outlined clearable></v-textarea>
        </div>
        <v-card-actions class="ma-4">
          <v-spacer></v-spacer>
          <v-btn color="#0095a8">Criar</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data() {
    return {
      isInit: true,
      isResponseAvailable: false,
    };
  },
  mounted() {
    fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.isInit = json.init;
      });
  },
};
</script>
