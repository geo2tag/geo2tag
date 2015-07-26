#!/bin/bash
function stopMachine(){
	local vmNameToStop=$1
	echo 'Saving and stopping machine '${vmNameToStop}
	VBoxManage controlvm ${vmNameToStop} acpipowerbutton
	while [ -z $(VBoxManage showvminfo ${vmNameToStop} | grep 'State:.*' | grep -o "off") ]; do
		echo $(VBoxManage showvminfo ${vmNameToStop} | grep 'State*')
		echo 'Waiting the machine for poweroff state'
		sleep 3
	done
	echo 'Machine is in poweroff state'
}
echo '--------------RESIZING STORAGE--------------'
vmPath=$HOME'/VirtualBox VMs/'
vmName=$(VBoxManage list runningvms | grep -o '"vagrant_default_.*"' | tr -d '"')
vmDiskName=$(ls "${vmPath}"${vmName}/ | grep -o '.*\.vmdk')
vmdkOldHdUUID=$(VBoxManage showhdinfo "${vmPath}"${vmName}'/'${vmDiskName} | head -1 | tr -d 'UUID: ')
stopMachine ${vmName} && wait
if [ ! -z ${vmDiskName} ]; then
	echo 'Cloning storage to vdi format'
	VBoxManage clonehd "${vmPath}"${vmName}'/'${vmDiskName} "${vmPath}"${vmName}'/storage.vdi' --format VDI | tr -d 'UUID: '	
fi
echo 'Resizing created vdi formatted storage to '$1' and attaching to vm '${vmName}
VBoxManage modifyhd "${vmPath}"${vmName}'/storage.vdi' --resize $1
VBoxManage storageattach ${vmName} --storagectl SATAController --port 0 --device 0 --type hdd --medium "${vmPath}"${vmName}'/storage.vdi'
if [ ! -z ${vmDiskName} ]; then
	vboxmanage closemedium disk ${vmdkOldHdUUID} --delete
fi
echo 'Starting machine '"${vmName}"
VBoxManage startvm ${vmName} --type headless
echo 'Waiting machine to full boot'
while : ; do
	VBoxManage guestcontrol ${vmName} exec /bin/pwd --wait-exit --username vagrant --password vagrant
	if [ $? -eq 0 ]; then break; fi
	sleep 3
done
echo 'Restarting machine'${vmnae}", so all memory will be available"
stopMachine ${vmName} && wait
VBoxManage startvm ${vmName} --type headless
echo '--------------------DONE--------------------'