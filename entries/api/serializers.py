from rest_framework import serializers



class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept= serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.DateTimeField()
    
    def create (self, validated_data):
        instance= Entry (
            datetime =  validated_data.get("datetime"),
            concept =   validated_data.get("concept"),
            amount =   validated_data.get("amount"),
        )
        instance.save()
        return instance
    
    def update(self):
        pass
    
    def delete(self):
        pass
