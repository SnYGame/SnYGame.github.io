module AutoLink
  class AutoLinkGenerator < Jekyll::Generator
    def generate(site)
      for auto_link in Jekyll.configuration({})["auto_link"] do
        link = auto_link["link"]
        for keyword in auto_link["keywords"] do
          regex = Regexp.new("^(?!# ).*(?![^\\[]*\\])\\K\\b%s\\b" % [keyword])
          for page in site.pages do
            if page.dir.start_with? "/game" then
              if page.url != "%s.html" % [link] then
                while page.content.match(regex) do
                  page.content = page.content.gsub(regex, "[%s](%s)" % ['\0', link])
                end
              else
                while page.content.match(regex) do
                  page.content = page.content.gsub(regex, "[%s](temp_remove)" % ['\0'])
                end
              end
            end
          end
        end
      end

      for page in site.pages do
        if page.dir.start_with? "/game" then
          page.content = page.content.gsub(/\[([^\[]+)\]\(temp_remove\)/, '\1').gsub(/(?<!# )(?<!#)\bv?((\d+)\.\d+\.\d+[b-z]?)\b/, '[\0](/game/changelog/v\2.html#v\1)')
        end
      end
    end
  end
end