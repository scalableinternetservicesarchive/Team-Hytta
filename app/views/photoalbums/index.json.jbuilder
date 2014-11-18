json.array!(@photoalbums) do |photoalbum|
  json.extract! photoalbum, :id, :name, :description, :picture
  json.url photoalbum_url(photoalbum, format: :json)
end
