json.array!(@todolists) do |todolist|
  json.extract! todolist, :id, :name
  json.url todolist_url(todolist, format: :json)
end
