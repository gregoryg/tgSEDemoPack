#!/bin/bash

gsql < ./packages/synthea/scripts/loadOrganizations.gsql
gsql < ./packages/synthea/scripts/loadEncounters.gsql
gsql < ./packages/synthea/scripts/loadPatientSymptoms.gsql
gsql < ./packages/synthea/scripts/loadImaging.gsql
gsql < ./packages/synthea/scripts/loadPayerTransitions.gsql
gsql < ./packages/synthea/scripts/loadImmunizations.gsql
gsql < ./packages/synthea/scripts/loadPayers.gsql
gsql < ./packages/synthea/scripts/loadProcedures.gsql
gsql < ./packages/synthea/scripts/loadAllergies.gsql
gsql < ./packages/synthea/scripts/loadMedications.gsql
gsql < ./packages/synthea/scripts/loadProviders.gsql
gsql < ./packages/synthea/scripts/loadAttributes.gsql
gsql < ./packages/synthea/scripts/loadObservations.gsql
gsql < ./packages/synthea/scripts/loadZips.gsql
gsql < ./packages/synthea/scripts/loadCareplans.gsql
gsql < ./packages/synthea/scripts/loadConditions.gsql
gsql < ./packages/synthea/scripts/loadPatient.gsql
gsql < ./packages/synthea/scripts/loadDevices.gsql

## gsql < ./packages/synthea/scripts/loadLocations.gsql
## gsql < ./packages/synthea/scripts/loadPatientNotes.gsql
